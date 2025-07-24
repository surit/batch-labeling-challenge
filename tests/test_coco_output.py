import json

def test_coco_json_structure():
    with open('/home/ubuntu/fish_detector/transformed_coco.json') as f:
        data = json.load(f)
    assert 'images' in data
    assert 'annotations' in data
    assert 'categories' in data
    assert isinstance(data['images'], list)
    assert isinstance(data['annotations'], list)
    assert isinstance(data['categories'], list)
    print("✅ COCO JSON structure test passed.")

if __name__ == "__main__":
    test_coco_json_structure()
