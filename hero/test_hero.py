#!/usr/bin/env python3
import hero
import command_pb2

if __name__ == "__main__":
	s = hero.setup("dani")
	if True:
		hero.init(10,10,0,0)

		c = command_pb2.Cmd()
		c.cmd = command_pb2.CmdType.MAP
		c.strings.append('coin')
		c.ints.append(3)
		c.ints.append(1)
		c.ints.append(2)
		c.ints.append(2)
		s.sendall(c.SerializeToString())
		s.recv(1024)

		hero.render()

	#dengine.setup(b'map;B;gen:A:10:10')
	hero.scan()
	while hero.canMoveDown():
		hero.moveDown()
	hero.moveRight()
	hero.moveUp()




