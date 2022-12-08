d=2022-07-14

while [ "$d" != 2022-12-08 ]; do 
  echo $d
  d=$(date -I -d "$d + 1 day")
  nd=$(echo $d | tr -d '-')
  echo $nd
  echo "../cam1/cam1-${nd}"
  if compgen -G "../cam1/cam1-${nd}_*.png" > /dev/null; then
    echo "${nd} exists!"
    ffmpeg -f image2 -framerate 30 -pattern_type glob -i "../cam1/cam1-${nd}_*" -s 1920x1080 -vcodec libx264 -crf 25 -pix_fmt yuv420p cam1-${nd}.mp4
  fi
  # mac option for d decl (the +1d is equivalent to + 1 day)
  # d=$(date -j -v +1d -f "%Y-%m-%d" $d +%Y-%m-%d)
done
