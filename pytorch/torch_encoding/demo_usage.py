# -*- coding: utf-8 -* -
'''
Pytorch Encoding工具集，主要包含各种分割模型
'''
import torch
import encoding

if __name__ == '__main__':
    # Get the model
    model = encoding.models.get_model("encnet_resnet101_ade", pretrained=True).cpu()
    model.eval()

    # Prepare the image
    img_path = "demo.jpg"
    img = encoding.utils.load_image(img_path).cpu().unsqueeze(0)

    # Make prediction
    output = model.evaluate(img)
    predict = torch.max(output, 1)[1].cpu().numpy() + 1

    # Get color pallete for visualization
    mask = encoding.utils.get_mask_pallete(predict, "pascal_voc")
    mask.save("demo_output.jpg")
