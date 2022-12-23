import numpy as np
from PIL import Image
from matplotlib.pyplot import imshow
import dbscan


def __main__():
   
        # Loading image:
        img_path = 'download.jpeg'
        img = Image.open(img_path)
        pixels = img.load()
        width, height = img.size
        # Turn image into list of vectors (1 vector / pixel):
        vector_list = []
        for x in range(width):
            for y in range(height):

                current_point = [pixels[x, y][0], pixels[x, y][1], pixels[x, y][2]]

                current_vector = np.array(current_point)

                vector_list.append(current_vector)


        print('Image file with dimensions {}x{} pixels turned into {} vectors.'.format(width, height, len(vector_list)))

        dbscan_clusters = dbscan.db_scan_algorithm(vector_list, 5, 5)

        def clusters_to_image(cluster_per_point_list: list, points: list, width, height):

            assert (len(cluster_per_point_list) == len(points))

            cluster_count = max(cluster_per_point_list) + 1

            inverted_clusters = [[] for _ in range(cluster_count)]

            for i in range(len(cluster_per_point_list)):

                inverted_clusters[cluster_per_point_list[i]].append(points[i])



            mean_colors = [np.array([0, 0, 0]) for _ in range(cluster_count)]
            counter = [0 for _ in range(cluster_count)]
            for i in range(cluster_count):
                for elem in inverted_clusters[i]:
                    mean_colors[i] = np.add(mean_colors[i], elem)
                    counter[i] += 1



                mean_colors[i] = np.divide(mean_colors[i], np.array([counter[i], counter[i], counter[i]]))

            clustered_image = Image.new('RGB', (width, height))

            pix = clustered_image.load()

            for x in range(width):

                for y in range(height):
                    cl_id = cluster_per_point_list[y + x * height]

                    if cl_id == -1:
                        pix[x, y] = (0, 0, 0)

                    else:
                        curr_pixel = [int(x) for x in mean_colors[cl_id]]
                        pix[x, y] = tuple(curr_pixel)


            return clustered_image

        clustered_image = clusters_to_image(dbscan_clusters, vector_list, width, height)

        # Displaying the clustered image:

        imshow(np.asarray(clustered_image))
  

       

__main__()
