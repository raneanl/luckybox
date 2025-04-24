from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# 선물 번호 지정 (예: 3개만 당첨)
gift_numbers = {
    3: {"name": "고화질 방셀(1475)", "image": "1475.png"},
    15: {"name": "치킨 기프티콘", "image": "치킨.png"},
    27: {"name": "스타벅스 기프티콘", "image": "starbucks.png"},
}

# 이미 선택된 번호 추적
used_numbers = set()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pick", methods=["POST"])
def pick():
    number = int(request.json.get("number"))

    if number in used_numbers:
        return jsonify({"status": "used"})

    used_numbers.add(number)

    prize = gift_numbers.get(number)
    if prize:
        return jsonify({"status": "win", "prize": prize})
    else:
        return jsonify({"status": "lose"})

if __name__ == "__main__":
    app.run(debug=True)
