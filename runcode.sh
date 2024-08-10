years=${1:-10}
dt=${2:-3600}

echo "Running Solar System Simulation..."
pypy main.py --years $years --dt $dt

echo "Animating Solar System Simulation..."
py animate.py