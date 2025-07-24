#from PIL import Image
#import albumentations as A
#import numpy as np

#transforms = A.load('transforms.json')
#image = np.array(Image.open('output.jpg'))
#image = transforms(image=image)['image']

# Now the image is preprocessed and ready to be accepted by the model

from PIL import Image
import albumentations as A
import numpy as np
import json
from datetime import datetime

# Load transformations
transforms = A.load('transforms.json')

# Initialize COCO format dictionary
coco_output = {
    "info": {
        "description": "Transformed Images",
        "date_created": datetime.now().isoformat(),
    },
    "images": [],
    "annotations": [],  # Empty since we're just transforming images
    "categories": []    # Empty unless you have class info
}

# Process image
image_path = 'output.jpg'
image = np.array(Image.open(image_path))

# Store original image info in COCO format
image_id = 1
coco_output["images"].append({
    "id": image_id,
    "file_name": image_path.split('/')[-1],
    "width": image.shape[1],
    "height": image.shape[0],
    "original_width": image.shape[1],
    "original_height": image.shape[0]
})

# Apply transformations
transformed = transforms(image=image)
transformed_image = transformed['image']

# Save transformed image
output_image_path = 'transformed_' + image_path.split('/')[-1]
Image.fromarray(transformed_image).save(output_image_path)

# Update COCO data with transformed image info
coco_output["images"][0].update({
    "transformed_width": transformed_image.shape[1],
    "transformed_height": transformed_image.shape[0],
    "transformed_path": output_image_path
})

# Save COCO format JSON
with open('transformed_coco.json', 'w') as f:
    json.dump(coco_output, f, indent=2)

print(f"Transformed image saved to {output_image_path}")
print(f"COCO format metadata saved to transformed_coco.json")
