"""_summary_

    Returns:
        string: string of the lobby id of Monster Hunter World
"""
import sys
import struct
import win32api
import win32process
import win32con

# ONLY WORKS WHEN THIS IS CHANGED
# https://github.com/vsantiago113/ReadWriteMemory/commit/e8b2859349e41380b561f6115ee43f058323877a
from ReadWriteMemory import ReadWriteMemory


def get_process_by_name(process_name):
    """Finds the process id of the given
    process name and returns the process id and its base address."""
    process_name = process_name.lower()
    # Enumerate all processes
    processes = win32process.EnumProcesses()
    for process_id in processes:
        # If process_id is the same as this program, skip it
        if process_id == -1:
            continue
        # Try to read the process memory
        try:
            h_process = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION 
                                             | win32con.PROCESS_ALL_ACCESS, True, process_id)
            # Try to read the modules of the process
            try:
                # modules is an array of base addresses of each module
                modules = win32process.EnumProcessModules(h_process)
                for base_address in modules:
                    # Get the name of the module
                    name = str(win32process.GetModuleFileNameEx(h_process, base_address))
                    # Compare it to the name of your program
                    if name.lower().find(process_name) != -1:
                        return process_id, base_address
            finally:
                win32api.CloseHandle(h_process)
        except:
            pass
def print_id():
    """_summary_
    """
    rwm = ReadWriteMemory()
    process = rwm.get_process_by_name('MonsterHunterWorld.exe')
    process.open()
    #print(process.__dict__)
    _, base_address = get_process_by_name('MonsterHunterWorld.exe')
    id_pointer = process.get_pointer(base_address + 0x050112F0,
                                     offsets=[0xAE8, 0xF0, 0x128, 
                                              0x58, 0xD0, 0x1D0, 0x208, 0x30, 0x3C8])
    answer = ""
    for x in range(3):
        # i read 4 symbols at a time, so you need to move X amoutn of times by 4
        id = process.read(id_pointer + x*4)
        #print(f"ID pointer: {hex(id_pointer)}")
        #print(id)
        struct_fmt = "{}s".format(4)
        # x7@p@D2R2h3@
        answer += str(struct.unpack(struct_fmt, struct.pack("@I", id))[0])[2:-1]
    process.close()
    return answer

def main():
    """_summary_
    """
    try:
        lobby_id =print_id()
    except:
        print("An exception has occured while trying to get the LobbyID")
    else:
        sys.stdout.write(lobby_id)
        sys.exit(0)


if __name__ == "__main__":
    main()
 