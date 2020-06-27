docker run \
  --rm \
  -p 8888:8888 \
  -v $PWD:/tf/course_material \
  tensorflow/tensorflow:latest-py3-jupyter