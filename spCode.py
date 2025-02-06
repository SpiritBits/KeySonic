live_loop :foo do
  use_real_time
  note, amp, pan = sync "/osc*/trigger/prophet"
  #Space-Taste
  sample :perc_bell, amp: rrand(0.2,1.2),pan: rrand(-1.0,1.0) if(note==55)
  # +* Taste
  sample :mehackit_phone4, amp: amp, pan: pan if(note==56)
  # '#' - Taste (Raute/Hashtag)
  sample :glitch_perc2, amp: amp, pan: pan if(note==57)
  # ESC - Taste (ESC-Taste ist irgendwie fehlerhaft, deshalb ist sie hier erstmal raus genommen.
  #sample :hat_snap,amp: rrand(0.8,1.0), pan: pan, rate: rrand(1.0,1.2) if( note == 58)
  # TAB - Taste
  sample :glitch_perc5,amp: rrand(0.8,1.0), pan: pan, rate: rrand(1.0,1.2) if( note == 59)
  # ä - Taste
  sample :hat_snap,amp: rrand(0.8,1.0), pan: pan, rate: rrand(1.0,1.2) if( note == 60)
  # . - Taste
  sample :tabla_tas2,amp: rrand(0.8,1.0), pan: pan, rate: rrand(1.0,1.2) if( note == 61)
  # , - Taste
  sample :tabla_tas1,amp: rrand(0.8,1.0), pan: pan, rate: rrand(1.0,1.2) if( note == 62)
  # ENTER
  sample :perc_bell2,amp: rrand(0.8,1.0), pan: pan, rate: rrand(1.0,1.2) if( note == 63)
  # UP
  sample :hat_snap,amp: rrand(0.8,1.0), pan: pan, rate: rrand(1.0,1.2) if( note == 64)
  # DOWN
  sample :hat_zan if( note == 65)
  # LEFT
  sample :hat_zap,amp: rrand(0.8,1.0), pan: pan, rate: rrand(1.0,1.2)  if( note == 66)
  # RIGHT
  sample :hat_tap,amp: rrand(0.8,1.0), pan: pan, rate: rrand(1.0,1.2)  if( note == 67)
  # backspace
  sample :perc_till,amp: rrand(0.8,1.0), pan: rrand(-0.8,0.8), rate: rrand(1.0,1.1) if( note == 68)
  # Tasten 1-0
  sample :bd_haus,amp: rrand(0.8,1.0), pan: pan, rate: rrand(1.0,1.2) if( note >= 70 and note <= 79)
  # Bindestrich
  sample :elec_twang, amp: rrand(0.8,1.0), pan: rrand(-1.0,1.0), rate: rrand(1.0,1.2) if( note == 80)
  # Alle Tasten, denen die Note 50 zugewiesen wurde, also alle anderen
  sample :drum_bass_soft  , amp: rrand(0.4,1.2), pan: pan, rate: rrand(1.5,2.5) if( note == 50)
  sample :drum_bass_soft   , amp: rrand(0.4,1.2), pan: pan, rate: rrand(1.5,2.5) if( note == 51)
  sample :drum_bass_soft , amp: rrand(0.4,1.2), pan: pan, rate: rrand(1.5,2.5) if( note == 52)
  #:drum_bass_soft
  sleep 0.01
end
