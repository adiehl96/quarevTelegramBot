import telepot
import wget
import time
import os, csv, argparse

parser = argparse.ArgumentParser(
    description="Quartus FPGA Bit Stream Reversal Tool Telegram Bot.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

parser.add_argument(
    "-t",
    "--token",
    required=True,
    help="Telegram Bot token, supplied by Botfather. See telepot docs for more info.",
    )

args = parser.parse_args()

def bitreverse(n):
    return int("{:08b}".format(n)[::-1], 2)

def open_csv(path_to_file):
    datasetfile = open(path_to_file)
    datasetreader = csv.reader(datasetfile, delimiter=",")
    csv_content = list(datasetreader)
    return csv_content

def process_csv(csv_content):
    return_string = ""
    for row in csv_content:
        for item in row:
            if item.lstrip().isnumeric():
                return_string += str(bitreverse(int(item))).rjust(3) + ","
        return_string += "\n"
    return return_string

def quarev(path_to_file):
  full_path = os.path.realpath(path_to_file)
  csv_content = open_csv(full_path)
  print("quarev: len(csv_content)", len(csv_content))
  return_string = process_csv(csv_content)
  with open("bitstream.h", "w") as text_file:
    text_file.write(return_string[:-2])

def handle_bitstream(file_id, chat_id):
  if os.path.exists("./bitstream.ttf"):
    os.remove("./bitstream.ttf")
  if os.path.exists("./bitstream.h"):
    os.remove("./bitstream.h")
  filepath = bot.getFile(file_id)['file_path']
  url = f'https://api.telegram.org/file/bot{args.token}/{filepath}'
  try:
    wget.download(url, out= f'bitstream.ttf')
    print("handle_bitstream: bitstream downloaded")
  except:
    print("handle_bitstream: couldn't download bitstream")
  quarev("./bitstream.ttf")
  bot.sendDocument(chat_id, open('./bitstream.h', 'rb'))


update_id_heap = []
while(True):
  time.sleep(0.1)
  bot = telepot.Bot(args.token)
  bot.getMe()
  response = bot.getUpdates()
  if len(response):
    response = response[-1]
  else:
    continue
  
  if not len(update_id_heap):
    update_id_heap.append(response["update_id"])
    continue
  if response["update_id"] in update_id_heap: continue
  update_id_heap.append(response["update_id"])
  chat_id = response["message"]["chat"]["id"]
  try:
    file_id = response["message"]["document"]["file_id"]
    handle_bitstream(file_id, chat_id)
    print("responded with new bitstream")
  except:
    bot.sendMessage(chat_id, "Hey there, I'm made for reversing Quartus FPGA bitstreams. Send a bitstream to me to see how it works.")
    print("no file detected")
