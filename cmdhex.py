import argparse



parser = argparse.ArgumentParser(
		description='A hex tool for modifying file.', 
		conflict_handler='resolve')


parser.add_argument('-f','--file', 
		type=argparse.FileType('rb'),
		required=True,
		help='the input file name.')


parser.add_argument('-p','--position', 
		type=int,
		required=True,
		help='the start address of writing postion. like 20, means the 20th bit of this file.')


parser.add_argument('-v','--value', 
		type=str,
		required=True,
		help='the hex data to write. like 504b0304')


parser.add_argument('-o','--output', 
		type=str,
		required=True,
		help='the output file after modify.')


args = parser.parse_args()


#zip_header = "504b0304"


if args.position < 1 :
	print(f"{args.position} is an invalid positive int value" )
	exit(-1)




with args.file:
	data = args.file.read()
	args.file.close()


with open(args.output,'wb') as fw:
	fw.write( data)
	fw.seek( args.position -1 )
	fw.write( bytes.fromhex( args.value) )
	fw.flush()
	fw.close()

#end_time = time.time()

print(f'Done with openning "{args.file.name}" , writting {args.value} at postion {args.position} and saving to "{args.output}"!')
