-- P1 HP Bar- 0x000D12 (actual health - 0x000C2B)
-- P2 HP Bar- 0X000F12 (other interest  actual health - 0x000E2B,  stun? 0x000E35)
-- P2 in the air - 0X0000B4, 0X0000B8
-- P1 in the air (a lot of memory addresses) - 0x000EB6
-- P2 crouching - 0X000E3A-F ? (1 is standing, 2 is crouch, 3 is jumping, 30+ is jf or jb)
-- Also maybe     0x000E44 (1 is crouch, 0 is not)
-- P2 attack - 0x000EB3 (1 indicates attack active, 0 indicates not active)
-- P2 attack type - 0x000EB8 0 is punch, 2 is kick)
-- 0x000ED5 ?
-- 0x000ED8 ? both also seem to relate to type of attack
-- 0x000524 fireball out or not

-- Potential interest: whether P1 or P2 is in blockstun
-- Distance between players - 0X000CB4
-- Round TIme - 0x001AC8

-- Game start
-- maybe 000CCE, 001A60


local function update_memory_values(memory_values)
    memory_values["p1_hp"] = memory.readbyte(0x000C2B)
    memory_values["p2_hp"] = memory.readbyte(0x000E2B)
    memory_values["p2_air"] = memory.readbyte(0x0000B4)
    memory_values["p2_crouch"] = memory.readbyte(0x000E3B)
    memory_values["p2_attacking"] = memory.readbyte(0x000EB3)
    memory_values["p2_attack_type"] = memory.readbyte(0x000EB8)
    memory_values["p2_fireball"] = memory.readbyte(0x000524)
    memory_values["distance"] = memory.readbyte(0x000CB4)
    memory_values["time"] = memory.readbyte(0x001AC8)
    memory_values["game_start"] = memory.readbyte(0x001A60)
end


local function set_input(buttons)
    joypad.set(buttons, 1)
end

-- testing to make sure that socket server is connected
comm.socketServerSend("hello world again!")

memory_values = {}
while true do
    savestate.loadslot(1)
    memory_values["game_start"] = memory.readbyte(0x001A60)
    while memory_values["game_start"] == 1 do
        update_memory_values(memory_values)
        -- this is where i would send the data to gym
        -- i.e, comm.socketServerSend("...")
        -- this is also where i would set the input recieved by gym
        -- i.e, comm.socketServerRecieve or response, i forgot
        set_input({Right=true})
        emu.frameadvance()
    end
    print("hello world")
    emu.frameadvance()
end