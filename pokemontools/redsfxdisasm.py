from __future__ import print_function
from __future__ import absolute_import
from . import configuration
config = configuration.Config()
rom = bytearray(open(config.rom_path, "r").read())

sfx_names = [
	"Snare1_2",
	"Snare2_2",
	"Snare3_2",
	"Snare4_2",
	"Snare5_2",
	"Triangle1_2",
	"Triangle2_2",
	"Snare6_2",
	"Snare7_2",
	"Snare8_2",
	"Snare9_2",
	"Cymbal1_2",
	"Cymbal2_2",
	"Cymbal3_2",
	"Muted_Snare1_2",
	"Triangle3_2",
	"Muted_Snare2_2",
	"Muted_Snare3_2",
	"Muted_Snare4_2",
	"Cry00_2",
	"Cry01_2",
	"Cry02_2",
	"Cry03_2",
	"Cry04_2",
	"Cry05_2",
	"Cry06_2",
	"Cry07_2",
	"Cry08_2",
	"Cry09_2",
	"Cry0A_2",
	"Cry0B_2",
	"Cry0C_2",
	"Cry0D_2",
	"Cry0E_2",
	"Cry0F_2",
	"Cry10_2",
	"Cry11_2",
	"Cry12_2",
	"Cry13_2",
	"Cry14_2",
	"Cry15_2",
	"Cry16_2",
	"Cry17_2",
	"Cry18_2",
	"Cry19_2",
	"Cry1A_2",
	"Cry1B_2",
	"Cry1C_2",
	"Cry1D_2",
	"Cry1E_2",
	"Cry1F_2",
	"Cry20_2",
	"Cry21_2",
	"Cry22_2",
	"Cry23_2",
	"Cry24_2",
	"Cry25_2",
	"Level_Up",
	"Get_Item2_2",
	"Tink_2",
	"Heal_HP_2",
	"Heal_Ailment_2",
	"Start_Menu_2",
	"Press_AB_2",
	"Ball_Toss",
	"Ball_Poof",
	"Faint_Thud",
	"Run",
	"Dex_Page_Added",
	"Caught_Mon",
	"Peck",
	"Faint_Fall",
	"Battle_09",
	"Pound",
	"Battle_0B",
	"Battle_0C",
	"Battle_0D",
	"Battle_0E",
	"Battle_0F",
	"Damage",
	"Not_Very_Effective",
	"Battle_12",
	"Battle_13",
	"Battle_14",
	"Vine_Whip",
	"Battle_16",
	"Battle_17",
	"Battle_18",
	"Battle_19",
	"Super_Effective",
	"Battle_1B",
	"Battle_1C",
	"Doubleslap",
	"Battle_1E",
	"Horn_Drill",
	"Battle_20",
	"Battle_21",
	"Battle_22",
	"Battle_23",
	"Battle_24",
	"Battle_25",
	"Battle_26",
	"Battle_27",
	"Battle_28",
	"Battle_29",
	"Battle_2A",
	"Battle_2B",
	"Battle_2C",
	"Psybeam",
	"Battle_2E",
	"Battle_2F",
	"Psychic_M",
	"Battle_31",
	"Battle_32",
	"Battle_33",
	"Battle_34",
	"Battle_35",
	"Battle_36",
	"Silph_Scope",
	"Snare1_1",
	"Snare2_1",
	"Snare3_1",
	"Snare4_1",
	"Snare5_1",
	"Triangle1_1",
	"Triangle2_1",
	"Snare6_1",
	"Snare7_1",
	"Snare8_1",
	"Snare9_1",
	"Cymbal1_1",
	"Cymbal2_1",
	"Cymbal3_1",
	"Muted_Snare1_1",
	"Triangle3_1",
	"Muted_Snare2_1",
	"Muted_Snare3_1",
	"Muted_Snare4_1",
	"Cry00_1",
	"Cry01_1",
	"Cry02_1",
	"Cry03_1",
	"Cry04_1",
	"Cry05_1",
	"Cry06_1",
	"Cry07_1",
	"Cry08_1",
	"Cry09_1",
	"Cry0A_1",
	"Cry0B_1",
	"Cry0C_1",
	"Cry0D_1",
	"Cry0E_1",
	"Cry0F_1",
	"Cry10_1",
	"Cry11_1",
	"Cry12_1",
	"Cry13_1",
	"Cry14_1",
	"Cry15_1",
	"Cry16_1",
	"Cry17_1",
	"Cry18_1",
	"Cry19_1",
	"Cry1A_1",
	"Cry1B_1",
	"Cry1C_1",
	"Cry1D_1",
	"Cry1E_1",
	"Cry1F_1",
	"Cry20_1",
	"Cry21_1",
	"Cry22_1",
	"Cry23_1",
	"Cry24_1",
	"Cry25_1",
	"Get_Item1_1",
	"Get_Item2_1",
	"Tink_1",
	"Heal_HP_1",
	"Heal_Ailment_1",
	"Start_Menu_1",
	"Press_AB_1",
	"Pokedex_Rating_1",
	"Get_Key_Item_1",
	"Poisoned_1",
	"Trade_Machine_1",
	"Turn_On_PC_1",
	"Turn_Off_PC_1",
	"Enter_PC_1",
	"Shrink_1",
	"Switch_1",
	"Healing_Machine_1",
	"Teleport_Exit1_1",
	"Teleport_Enter1_1",
	"Teleport_Exit2_1",
	"Ledge_1",
	"Teleport_Enter2_1",
	"Fly_1",
	"Denied_1",
	"Arrow_Tiles_1",
	"Push_Boulder_1",
	"SS_Anne_Horn_1",
	"Withdraw_Deposit_1",
	"Cut_1",
	"Go_Inside_1",
	"Swap_1",
	"59_1",
	"Purchase_1",
	"Collision_1",
	"Go_Outside_1",
	"Save_1",
	"Pokeflute",
	"Safari_Zone_PA",
	"Snare1_3",
	"Snare2_3",
	"Snare3_3",
	"Snare4_3",
	"Snare5_3",
	"Triangle1_3",
	"Triangle2_3",
	"Snare6_3",
	"Snare7_3",
	"Snare8_3",
	"Snare9_3",
	"Cymbal1_3",
	"Cymbal2_3",
	"Cymbal3_3",
	"Muted_Snare1_3",
	"Triangle3_3",
	"Muted_Snare2_3",
	"Muted_Snare3_3",
	"Muted_Snare4_3",
	"Cry00_3",
	"Cry01_3",
	"Cry02_3",
	"Cry03_3",
	"Cry04_3",
	"Cry05_3",
	"Cry06_3",
	"Cry07_3",
	"Cry08_3",
	"Cry09_3",
	"Cry0A_3",
	"Cry0B_3",
	"Cry0C_3",
	"Cry0D_3",
	"Cry0E_3",
	"Cry0F_3",
	"Cry10_3",
	"Cry11_3",
	"Cry12_3",
	"Cry13_3",
	"Cry14_3",
	"Cry15_3",
	"Cry16_3",
	"Cry17_3",
	"Cry18_3",
	"Cry19_3",
	"Cry1A_3",
	"Cry1B_3",
	"Cry1C_3",
	"Cry1D_3",
	"Cry1E_3",
	"Cry1F_3",
	"Cry20_3",
	"Cry21_3",
	"Cry22_3",
	"Cry23_3",
	"Cry24_3",
	"Cry25_3",
	"Get_Item1_3",
	"Get_Item2_3",
	"Tink_3",
	"Heal_HP_3",
	"Heal_Ailment_3",
	"Start_Menu_3",
	"Press_AB_3",
	"Pokedex_Rating_3",
	"Get_Key_Item_3",
	"Poisoned_3",
	"Trade_Machine_3",
	"Turn_On_PC_3",
	"Turn_Off_PC_3",
	"Enter_PC_3",
	"Shrink_3",
	"Switch_3",
	"Healing_Machine_3",
	"Teleport_Exit1_3",
	"Teleport_Enter1_3",
	"Teleport_Exit2_3",
	"Ledge_3",
	"Teleport_Enter2_3",
	"Fly_3",
	"Denied_3",
	"Arrow_Tiles_3",
	"Push_Boulder_3",
	"SS_Anne_Horn_3",
	"Withdraw_Deposit_3",
	"Cut_3",
	"Go_Inside_3",
	"Swap_3",
	"59_3",
	"Purchase_3",
	"Collision_3",
	"Go_Outside_3",
	"Save_3",
	"Intro_Lunge",
	"Intro_Hip",
	"Intro_Hop",
	"Intro_Raise",
	"Intro_Crash",
	"Intro_Whoosh",
	"Slots_Stop_Wheel",
	"Slots_Reward",
	"Slots_New_Spin",
	"Shooting_Star",
	]

banks = {
	0x02: 0x60,
	0x08: 0x78,
	0x1f: 0x68,
	}

music_commands = {
	0xd0: ["notetype", {"type": "nibble"}, 2],
	0xe0: ["octave", 1],
	0xe8: ["toggleperfectpitch", 1],
	0xea: ["vibrato", {"type": "byte"}, {"type": "nibble"}, 3],
	0xec: ["duty", {"type": "byte"}, 2],
	0xed: ["tempo", {"type": "word"}, 3],
	0xf0: ["volume", {"type": "nibble"}, 2],
	0xf8: ["executemusic", 1],
	0xfc: ["dutycycle", {"type": "byte"}, 2],
	0xfe: ["loopchannel", {"type": "byte"}, {"type": "label"}, 4],
	0xff: ["endchannel", 1],
	}

param_lengths = {
	"nibble": 1,
	"byte": 1,
	"word": 2,
	"label": 2,
	}

music_notes = {
	0x0: "C_",
	0x1: "C#",
	0x2: "D_",
	0x3: "D#",
	0x4: "E_",
	0x5: "F_",
	0x6: "F#",
	0x7: "G_",
	0x8: "G#",
	0x9: "A_",
	0xa: "A#",
	0xb: "B_",
	}

sfxnum = 0

for bank in banks:
	print(bank)
	header = bank * 0x4000 + 3
	for sfx in range(1,banks[bank]):
		sfxname = sfx_names[sfxnum]
		sfxfile = open("music/sfx/" + sfx_names[sfxnum].lower() + ".asm", 'w')
		sfxname = "SFX_" + sfxname
		startingaddress = rom[header + 2] * 0x100 + rom[header + 1] + (0x4000 * (bank - 1))
		end = 0
		curchannel = 1
		lastchannel = (rom[header] >> 6) + 1
		channelnumber = rom[header] % 0x10
		output = ''
		while 1:
			address = startingaddress
			if curchannel != lastchannel:
				end = rom[header + 5] * 0x100 + rom[header + 4] + (0x4000 * (bank - 1))
			byte = rom[address]
			if byte == 0xf8 or (bank == 2 and sfx == 0x5e): executemusic = True
			else: executemusic = False
			output += "{}_Ch{}: ; {:02x} ({:0x}:{:02x})\n".format(sfxname, curchannel, address, bank, address % 0x4000 + 0x4000)
			while 1:
				if address == 0x2062a or address == 0x2063d or address == 0x20930:
					output += "\n{}_branch_{:02x}:\n".format(sfxname, address)
				if byte == 0x10 and not executemusic:
					output += "\tunknownsfx0x{:02x} {}".format(byte, rom[address + 1])
					command_length = 2
				elif byte < 0x30 and not executemusic:
					if channelnumber == 7:
						output += "\tunknownnoise0x20 {}, {}, {}".format(byte % 0x10, rom[address + 1], rom[address + 2])
						command_length = 3
					else:
						output += "\tunknownsfx0x20 {}, {}, {}, {}".format(byte % 0x10, rom[address + 1], rom[address + 2], rom[address + 3])
						command_length = 4
				elif byte < 0xc0:
					output += "\t{} {}".format(music_notes[byte >> 4], byte % 0x10 + 1)
					command_length = 1
				elif byte < 0xd0:
					output += "\trest {}".format(byte % 0x10 + 1)
					command_length = 1
				else:
					if byte < 0xe0:
						command = music_commands[0xd0]
						output += "\t{} {},".format(command[0], byte % 0x10)
						byte = 0xd0
					elif byte < 0xe8:
						command = music_commands[0xe0]
						output += "\t{} {}".format(command[0], 0xe8 - byte)
						byte = 0xe0
					else:
						command = music_commands[byte]
						output += "\t{}".format(command[0])
					command_length = 1
					params = 1
					# print all params for current command
					while params != len(music_commands[byte]) - 1:
						param_type = music_commands[byte][params]["type"]
						address += command_length
						command_length = param_lengths[param_type]
						param = rom[address]
						if param_type == "nibble":
							output += " {}, {}".format(param >> 4, param % 0x10)
						elif param_type == "byte":
							output += " {}".format(param)
						elif param_type == "word":
							output += " {}".format(param * 0x100 + rom[address + 1])
						else:
							param += rom[address + 1] * 0x100 - 0x4000 + (bank * 0x4000)
							if param == startingaddress: output += " {}_Ch{}".format(sfxname, curchannel)
							else: output += " {}_branch_{:02x}".format(sfxname, param)
						params += 1
						if params != len(music_commands[byte]) - 1: output += ","
				output += "\n"
				address += command_length
				if byte == 0xff or address == end: break
				byte = rom[address]
			header += 3
			channelnumber = rom[header]
			if curchannel == lastchannel:
			#	output += "; {}".format(hex(address))
				sfxfile.write(output)
				break
			output += "\n\n"
			startingaddress = address
			curchannel += 1
		sfxnum += 1