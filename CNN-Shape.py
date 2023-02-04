

input_size_h = 240
input_size_w = 320
padding_size = 0
filter_h = 5
filter_w = 5
stride = 2


def conv_output_size(input_size_h,input_size_w,padding_size,filter_h,filter_w,stride):
    Oh = (input_size_h + padding_size * 2 - filter_h)/stride + 1
    Ow = (input_size_w + padding_size * 2 - filter_w)/stride + 1
    return Oh, Ow


Oh,Ow = conv_output_size(input_size_h,input_size_w,padding_size,filter_h,filter_w,stride)
print(f"output_height: {int(Oh)},output_width: {int(Ow)}")