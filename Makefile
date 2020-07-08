graph.png: graph.dot
	dot $< -Tpng > $@

clean:
	$(RM) *~
