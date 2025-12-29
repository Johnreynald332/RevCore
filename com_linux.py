import subprocess as sp

def gathering():
    user = sp.run(["whoami"], capture_output=True, text=True)
    print("===username===")
    print(user.stdout)

    dis_env = sp.run(["env", "|", "grep", "-Ei", "key|token|secret"],capture_output=True, text=True)
    print("===display_env===")
    print(dis_env.stdout)

    check_writeable = sp.run(["find", "/", "-writeable", "-user", "root", "-type", "f", "2>/dev/null"],
                             capture_output=True, text=True)
    print("===check writeable owned by root===")
    print(check_writeable.stdout)

    check_kernel = sp.run(["uname","-a"],capture_output=True, text=True)
    print("===check_kernel===")
    print(check_kernel.stdout)

    all_user = sp.run(["who"],capture_output=True, text=True)
    print("===all_user===")
    print(all_user.stdout)

    bash_history = sp.run(["cat","~/.bash_history", "2>/dev/null"],capture_output=True, text=True)
    print("bash_history")
    print(bash_history.stdout)

    list_net = sp.run(["ss","-tulnp","||","netstat","-tulnp"],capture_output=True,text=True)
    print("===list_network===")
    print(list_net.stdout)

    process_run = sp.run(["ps","aux","|","grep","-Ei","'root|pass|ssh|key'"],capture_output=True, text=True)
    print("===process===")
    print(process_run.stdout)




