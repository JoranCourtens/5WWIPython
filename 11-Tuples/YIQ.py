def yiq(rgb):
    yiq_1 = rgb[0] * 0.299 + rgb[1] * 0.587 + rgb[2] * 0.114
    yiq_2 = rgb[0] * 0.596 + rgb[1] * -0.274 + rgb[2] * -0.322
    yiq_3 = rgb[0] * 0.211 + rgb[1] * -0.523 + rgb[2] * 0.312
    return (yiq_1, yiq_2, yiq_3)


