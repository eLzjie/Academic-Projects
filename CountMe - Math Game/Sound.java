package Audio;

import java.io.IOException;
import java.net.URL;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.LineEvent;
import javax.sound.sampled.LineListener;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.UnsupportedAudioFileException;

public class Sound {

    private final URL correct;
    private final URL wrong;
    private final URL click;
    private final URL music;
    private boolean muted;
    private Clip clip;

    public Sound() {
        this.correct = this.getClass().getClassLoader().getResource("Audio/correct_sound.wav");
        this.wrong = this.getClass().getClassLoader().getResource("Audio/wrong_answer.wav");
        this.click = this.getClass().getClassLoader().getResource("Audio/click_sound.wav");
        this.music = this.getClass().getClassLoader().getResource("Audio/bg_music.WAV");
        this.muted = false; 
        
    }


    public void soundCorrect(boolean muted) {
        if (!muted) {
            play(correct);
            System.out.println("Sound is");
        }else{
            clip.stop();
        }
    }

    public void soundWrong(boolean muted) {
        if (!muted) {
            play(wrong);
        }else{
            clip.stop();
        }
    }

    public void soundClick(boolean muted) {
        if (!muted) {
            play(click);
        }else{
            clip.stop();
        }
    }

    public void soundMusic() {
        if (!muted) {
            playMusic();
        }else{
            if (clip != null && clip.isRunning()) {
                clip.stop();
            }
        }
    }
    
        

    private void play(URL url) {
        try {
            AudioInputStream audioIn = AudioSystem.getAudioInputStream(url);
            Clip clip = AudioSystem.getClip();
            clip.open(audioIn);
            clip.addLineListener(new LineListener() {
                @Override
                public void update(LineEvent event) {
                    if (event.getType() == LineEvent.Type.STOP) {
                        clip.close();
                    }
                }
            });
            audioIn.close();
            clip.start();
        } catch (IOException | LineUnavailableException | UnsupportedAudioFileException e) {
            System.err.println(e);
        }
    }
    
    private void playMusic() {
        try {
            AudioInputStream audioIn = AudioSystem.getAudioInputStream(this.music);
            clip = AudioSystem.getClip();
            clip.open(audioIn);
            clip.loop(Clip.LOOP_CONTINUOUSLY); 
            clip.start();
        } catch (IOException | LineUnavailableException | UnsupportedAudioFileException e) {
            System.err.println(e);
        }
    }

    public void endMusic() {
        clip.stop();
    }    
    
    public void pauseMusic() {
        if (clip != null && clip.isRunning()) {
            clip.stop();
        }
    }
    
    public void resumeMusic() {
        if (clip != null && !clip.isRunning()) {
            clip.start();
        }
    } 
   
 
}



