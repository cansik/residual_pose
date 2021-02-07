import pyrealsense2 as rs
import numpy as np
import time

try:
    i = 0
    recording = False

    pipeline = rs.pipeline()
    pipeline.start()

    while True:
        frames = pipeline.wait_for_frames()
        depth = frames.get_depth_frame()
        if not depth: continue

        depth_image = np.asanyarray(depth.get_data())

        print("dev frame %d receiveid!" % i)

        if i == 100:
            print("recording!")
            recording = True

        if recording:
            np.save("img_samples/realsense/frame_%04d.npy" % i, depth_image)

        i += 1
    pipeline.stop()
    exit(0)
except Exception as e:
    print(e)
    pass