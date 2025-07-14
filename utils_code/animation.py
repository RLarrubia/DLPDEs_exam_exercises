import imageio.v2 as imageio
import shutil
import os

def create_animation(animation_name='Model_A_animation'):
    if os.path.exists('model_A_frames'):
        os.makedirs('Results', exist_ok=True)
        os.makedirs('Results/Animations', exist_ok=True)
        with imageio.get_writer(f"Results/Animations/{animation_name}.gif", mode="I", duration=0.1, loop=0) as writer:
            for i in range(len(os.listdir('model_A_frames'))):
                filename = f"model_A_frames/frame_{i:03d}.png"
                image = imageio.imread(filename)
                writer.append_data(image)
        shutil.rmtree('model_A_progress')
        shutil.rmtree('Model_A_frames')

