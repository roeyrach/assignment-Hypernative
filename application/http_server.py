from flask import Flask, request, jsonify
from etherscan_scraping import get_data_from_address

app = Flask(__name__)


@app.route('/', methods=['POST'])
def default():
    # list_of_labels = []
    # addresses = []
    # request_data = request.get_json()
    # for address in request_data:
    #     addresses.append(address)
    #     list_of_labels.append(get_data_from_address(address))
    # return jsonify(list_of_labels)

    # with one line code same as above
    return jsonify([get_data_from_address(address) for address in request.get_json()])


if __name__ == '__main__':
    app.run(debug=True, port=5000)
