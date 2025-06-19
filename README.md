# Control Dataset for VLBiasBench
###### Alex Lalov

Public repository for DSAIT4205 Fundamental Research in Machine Learning featuring a control dataset for VLBiasBench

All of the images in the `data/` directory will be noised and placed in the `noisy/` directory; simply run `python main.py`.
The python dependencies are in requirements.txt and it is recommended to use python 3.10.4 and execute the script while your working directory is the root of the repository.

#### Warning 
This repo includes the images and data since they are not substantially large


## Summary of Paper
[VLBiasBench](https://arxiv.org/pdf/2406.14194) is a proposed benchmark for determining how biased a Large Vision-Language Model *(LVLM)* is, through an accuracy scoring on both open and close-ended questions regarding various protected characteristics, e.g., Religion, Ethnicity, Disability. Both diffusion-generated images and text are provided as context to the model for both datasets and the model's response determines performance. Gauging this performance for the open-ended dataset is done through the VADER evaluation metric whereas the close-ended dataset is solely the percentage of correct answers. 

The simplicity of the close-ended dataset alongside the fact that it includes a "non-answer" option for the model makes it a good base for a control dataset that tests the benchmark's ability to determine bias if only some visual information is provided.

For context, these are the close-ended dataset's answers: 
* ( A ) Yes
* ( B ) No 
* ( C ) Not enough information

## Tested Property
There is an inherent assumption the paper makes, concerning both datasets: that the diffusion-generated images will always be relevant to the protected characteristic we are evaluating and that the model is making its decision by leveraging both image and text information equally. The latter is the key focus of this control dataset, as the property being tested is whether the models are  exploiting solely the provided question and context, while ignoring the image.

To what extent does the proposed [VLBiasBench](https://arxiv.org/pdf/2406.14194) test a LVLM's ability to display bias from its vision capabilities compared to its language understanding? Is the benchmark robust to models exploiting the provided context from the question formulation and answers?

## Dataset Creation

To test whether the models are using the question to primarily phrase and construct their answers, the control dataset will include some of the original images as a baseline with varying amounts of Gaussian noise added to them. The choice of Gaussian noise is significant compared to alternative noising methods such as uniform, salt-and-pepper and Poisson; Gaussian noise levels are more easily parameterized through just an adjustment of the distribution's standard deviation, while also being the basis for the same diffusion models that generated the images.

Creating the dataset was relatively simple as it required noising the original images to 1e2, 1e3 and 1e4 standard deviations, with mean 0. This creates three noised images: one that has removed some of the color of the underlying image, another that has almost removed all form and color and lastly an image of pure noise. Importantly, when noised at 1e3, the images still have a very slight outline which could be used by the model.


![noised_bias](https://hackmd.io/_uploads/SJKNNCCmee.png)

This process was performed on 20 images for the Race and Ethnicity protected characteristic creating a dataset of 80 images. Though the dataset alone isn't enough to perform the experiment.

## Testing Procedure

The images would be provided to the model alongside the same questions from the close-ended dataset, and in increasing order of noise, we would detect when the LVLM changes its mind from a positive ( A ) or negative ( B ) to the ( C ) "Not enough information" answer. The paper's hypothesis and claim that the benchmark is able to determine the visual bias of a model will hold if, and only if, for all fully noised images the model's response is ( C ). Furthermore, the degree of noise that is required for the LVLM to conclude ( C ) can also be evaluated to help determine just how much visual information is required for the model to claim it either knows or understands the problem.

## Implementation and Reproduction

The code which was used to generate the control dataset is available on [GitHub](https://github.com/Alex-Lalov/vlbiasbench-control).
