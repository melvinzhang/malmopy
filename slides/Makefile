ai-malmo.html: ai-malmo.md
	pandoc -t revealjs -s -o $@ \
	-V theme=white \
	-V revealjs-url=https://revealjs.com \
	-c custom.css $^

ai-malmo-local.html: ai-malmo.md
	pandoc -t revealjs -s -o $@ \
	-V theme=white \
	-c custom.css $^
