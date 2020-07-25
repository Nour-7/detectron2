def color_cmp (c1, c2):
  for i in range(len(c1)):
      if(c1[i] >= c2[i] + 5 or c1[i] <= c2[i] - 5):
        return False

  return True

def is_in_colorset(color):
  colorset = [ 
       [128, 18, 82],
       [37, 37, 205],
       [203, 203, 62],
       [197, 36, 36],
       [ 124, 124, 100],
       [106, 178, 117]]
  for c in colorset:
    if color_cmp(c, color) == True:
      return True
  return False

def recursive_mask(img, row, col, mask_radius, seed = 1):
  # edges of outer box
  # left = (row - mask_radius - seed) < 0 ? 0 : (row - mask_radius - seed)
  left =  0 if ((row - mask_radius - seed) < 0) else (row - mask_radius - seed)
  right = img.shape[0] - 1 if ((row + mask_radius + seed) >= img.shape[0]) else (row + mask_radius + seed)
  up =  0 if ((col - mask_radius - seed) < 0 ) else (col - mask_radius - seed) 
  down =  img.shape[1] -1 if (col + mask_radius + seed >= img.shape[1]) else (col + mask_radius + seed)
  # edges of inner box
  inner_left = row - mask_radius
  inner_right = row + mask_radius
  inner_up = col - mask_radius
  inner_down = col + mask_radius

  freq_color = {}
  for i in range(left, right):
    for j in range(up, down):
      #if the index inside the inner box
      if(i <= inner_right and i >= inner_left or
         j <= inner_up and j >= inner_down):
        continue;
      # count the colors
      if(is_in_colorset(img[i][j]) == True):
        key = (img[i][j][0], img[i][j][1], img[i][j][2])
        if(key in freq_color):
          freq_color[key] += 1
        else:
          freq_color[key] = 1

  if  bool(freq_color) == True: 
    max_key = max(freq_color.items(), key=operator.itemgetter(1))[0]
    return [max_key[0], max_key[1], max_key[2]]
  else: 
    return recursive_mask(img, row, col, mask_radius + seed, seed)

def mask_coloring(img, mask_radius, row, col):
  freq_color = {}
  start_row = row - mask_radius
  end_row = row + mask_radius + 1
  start_col = col - mask_radius
  end_col = col - mask_radius + 1

  if(is_in_colorset(img[row][col]) == True):
    return img[row][col]
    
  for i in range(start_row, end_row):
    for j in range(start_col, end_col):
      if(is_in_colorset(img[i][j]) == True):
        key = (img[i][j][0], img[i][j][1], img[i][j][2])
        if(key in freq_color):
          freq_color[key] += 1
        else:
          freq_color[key] = 1
  #max
  if  bool(freq_color) == True: 
    max_key = max(freq_color.items(), key=operator.itemgetter(1))[0]
    return [max_key[0], max_key[1], max_key[2]]
  else:
    seed = 2
    return recursive_mask(img, row, col, mask_radius, seed)

def max_filter(img, padding_pixels = 5):

  img_padded = img
  rows = img_padded.shape[0]
  cols = img_padded.shape[1]  
  img_padded = cv2.copyMakeBorder(img_padded, padding_pixels, padding_pixels, padding_pixels, padding_pixels, cv2.BORDER_CONSTANT, None, [0,0,0])

  for i in range(padding_pixels, rows + padding_pixels):
    for j in range(padding_pixels, cols + padding_pixels):
      img_padded[i][j] = mask_coloring(img_padded, padding_pixels, i, j)

  img_padded = img_padded[padding_pixels:img_padded.shape[0] - padding_pixels, padding_pixels:img_padded.shape[1] - padding_pixels ] 
  return img_padded

  
def image_segmentation(predictor, src_folder, des_folder, area_threshold):
  for filename in glob.glob(src_folder+'/*'):
      name = filename.split("/")[-1]
      print(name)
      im = cv2.imread(filename)
      # cv2_imshow(im)
      sem_seg = predictor(im)["sem_seg"].argmax(dim=0)
      v = Visualizer(im[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2)
      out = v.draw_sem_seg(sem_seg.to("cpu"),area_threshold= area_threshold, alpha=1.0)
      cv2.imwrite(des_folder + "withblack-"+ name  , out.get_image()[:, :, ::-1]) 
      im_out = max_filter(out.get_image()[:, :, ::-1], 5)
      cv2.imwrite(des_folder + name, im_out) 
