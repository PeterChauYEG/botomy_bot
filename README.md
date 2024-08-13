python -m venv venv
source venv/bin/activate

fastapi dev src/server.py --port 3000
python src/learn.py
python src/play.py

python src/test_gui.py

tensorboard --logdir ./tensorboard
# botomy_bot
