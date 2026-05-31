#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LOG_FILE="/tmp/pomodoro.log"

# 杀掉旧进程
pkill -f "番茄钟.py" 2>/dev/null

# 启动番茄钟，输出到日志
cd "$SCRIPT_DIR"
/usr/bin/python3 番茄钟.py > "$LOG_FILE" 2>&1 &

sleep 1

# 根据日志输出判断是否成功
if grep -q "番茄钟已启动" "$LOG_FILE" 2>/dev/null; then
    echo "✅ 番茄钟已在浏览器中打开"
    echo "   关闭此窗口不会影响番茄钟运行"
    read -p "   按 Enter 彻底退出番茄钟..."
    pkill -f "番茄钟.py" 2>/dev/null
else
    echo "❌ 启动失败，错误信息："
    cat "$LOG_FILE"
    read -p "按 Enter 关闭..."
fi
