WIN = windows
LIN = linux
SCRIPT = game.py
WIN_EXE = --onefile $(SCRIPT) --distpath $(WIN) --workpath $(WIN) --specpath $(WIN) --clean
LIN_EXE = --onefile $(SCRIPT) --distpath $(LIN) --workpath $(LIN) --specpath $(LIN) --clean
BUILD_LIN = pyinstaller --onefile $(SCRIPT) -n game_lin


lin:
	mkdir -p lin
	@echo "Сборка для Linux..."
	@if $(BUILD_LIN); then \
		mv dist/game_lin lin/; \
		rm -rf build dist game_lin.spec __pycache__; \
	else \
		echo "Ошибка при сборке для Linux"; \
	fi


windows:
	mkdir $(WIN)
	pip install pyinstaller
	pyinstaller $(WIN_EXE)
	./$(WIN)/Game.exe

web: game.py
	@echo "Creating game.html..."
	@echo "<!DOCTYPE html>" > game.html
	@echo "<html lang=\"en\">" >> game.html
	@echo "<head>" >> game.html
	@echo "<meta charset=\"UTF-8\">" >> game.html
	@echo "<title>Title</title>" >> game.html
	@echo "<link rel=\"stylesheet\" href=\"https://pyscript.net/latest/pyscript.css\" />" >> game.html
	@echo "<script defer src=\"https://pyscript.net/latest/pyscript.js\"></script>" >> game.html
	@echo "</head>" >> game.html
	@echo "<body>" >> game.html
	@echo "<h1>game</h1>" >> game.html
	@echo "<py-script>" >> game.html
	type game.py >> game.html
	@echo "</py-script>" >> game.html
	@echo "</body>" >> game.html
	@echo "</html>" >> game.html
	@echo "game.html created successfully."



clean:
	rm -rf win lin

clean:
	rm -rf $(WIN)
	rm -rf $(LIN)
