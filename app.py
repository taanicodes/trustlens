from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def alert():
    data = request.get_json()
    video_status = data.get('status')
    if video_status == 'fake':
        return jsonify({'message': 'Deepfake detected! Take action.'})
    return jsonify({'message': 'Video is authentic.'})

if __name__ == '__main__':
    app.run(debug=True)

def process_video(video_path):
    # Step 1: Extract frames
    output_folder = './frames'
    frame_count = extract_frames(video_path, output_folder)

    # Step 2: Load pre-trained model
    model = create_model()
    model.load_weights('path_to_pretrained_model_weights')

    # Step 3: Check each frame for deepfake
    fake_count = 0
    for i in range(frame_count):
        frame_path = f"{output_folder}/frame{i}.jpg"
        prediction = predict_deepfake(model, frame_path)
        if prediction > 0.5:  # 0.5 is the threshold
            fake_count += 1

    # Step 4: Store video hash on blockchain
    receipt = store_video_hash(video_path)

    # Step 5: Return results and blockchain receipt
    if fake_count > frame_count / 2:
        return {'status': 'fake', 'receipt': receipt}
    return {'status': 'real', 'receipt': receipt}
