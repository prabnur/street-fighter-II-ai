start cmd.exe /k python Python/train_agent.py
timeout 15
cd "emulator and rom/BizHawk-2.5.2"
Emuhawk.exe --socket_ip=127.0.0.1 --socket_port=8080