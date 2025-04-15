from onnx2tf import convert

# Define the paths
onnx_model_path = "/home/admin1/Downloads/best.onnx"
output_tf_path = "/home/admin1/Downloads/best_tf_model"  # This will be a folder

# Run the conversion
convert(
    input_onnx_file_path=onnx_model_path,
    output_folder_path=output_tf_path,
    copy_onnx_input_output_names_to_tflite=True  # Optional: useful if you'll convert to TFLite later
)

print(f"Model converted and saved to: {output_tf_path}")
