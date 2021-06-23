echo "<(^.^<) <(^.^)> (>^.^)>"
cd /mnt/input_data/input_data
pwd
ls -la
echo "input_file is ${INPUT_FILE}"
ls -la ${INPUT_FILE}
echo "output dir is : ${OUTPUT_DIR}"
mkdir ${OUTPUT_DIR}
RANDOM_NUMBER=$RANDOM
FILENAME="${OUTPUT_DIR}/$RANDOM_NUMBER.tmp"
echo "why would you even look in here??!!!!" > $FILENAME
cd ${OUTPUT_DIR}
ls -la
pwd
