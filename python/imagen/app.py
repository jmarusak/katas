from vertexai.preview.vision_models import ImageGenerationModel

prompt = "Create simple image of a horse head in Alphonse Mucha style."

image_model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-001")
images = image_model.generate_images(
    prompt=prompt,
    number_of_images=2,
    language="en",
    seed=100,
    add_watermark=False,
    aspect_ratio="1:1",
    safety_filter_level="block_few",
)

for i, img in enumerate(images):
    local_file_path = f"image_{i + 1}.png"
    img.save(local_file_path, include_generation_parameters=False)
