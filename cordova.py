from subprocess import PIPE, Popen
cmds = ['cd hello', 'cordova platform add android']
#This command could have multiple commands separated by a new line \n
process = Popen(
    ['cordova', 'create', 'hello', 'com.example.hello', 'HelloWorld'], stdout=PIPE, stderr=PIPE,stdin=None, shell=True)
stdout, stderr = process.communicate()
errcode = process.returncode
print(stdout)
print(stderr)
print(errcode)
if errcode == 0:
    insideFolder = Popen('cd hello & cordova platform add android', stdout=PIPE, stderr=PIPE,stdin=None, shell=True)
    ifout, iferr = insideFolder.communicate()
    iferrcode = insideFolder.returncode
    print(ifout)
    print(iferr)
    if iferrcode == 0:
        runAndroid = Popen('cd hello & cordova run android', stdout=PIPE, stderr=PIPE,stdin=None, shell=True)
        raout, raerr = runAndroid.communicate()
        print(raout)
        print(raerr) 
     



# p = subprocess.Popen(some_command,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)

# (output, err) = p.communicate()  
# print(output)
# for s_line in result.stdout:
#     #Parse it the way you want
#     out += s_line
#     print( s_line.rstrip())
# #This makes the wait possible
# p_status = p.wait()

# #This will give you the output of the command being executed
# print("Command output: ", output)