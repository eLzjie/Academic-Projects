/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package countme;

/**
 *
 * @author Huawei
 */
public class tutorial extends javax.swing.JFrame {

    /**
     * Creates new form tutorial
     */
    public tutorial() {
        initComponents();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        home = new javax.swing.JPanel();
        okay_btn = new javax.swing.JButton();
        jLabel2 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jLabel1 = new javax.swing.JLabel();
        background = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setPreferredSize(new java.awt.Dimension(800, 625));
        setResizable(false);
        setSize(new java.awt.Dimension(800, 625));

        home.setBackground(new java.awt.Color(86, 45, 128));
        home.setPreferredSize(new java.awt.Dimension(800, 600));
        home.setLayout(null);

        okay_btn.setIcon(new javax.swing.ImageIcon(getClass().getResource("/countme/Images/okay_btn.png"))); // NOI18N
        okay_btn.setBorder(null);
        okay_btn.setContentAreaFilled(false);
        okay_btn.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                okay_btnActionPerformed(evt);
            }
        });
        home.add(okay_btn);
        okay_btn.setBounds(340, 480, 120, 46);

        jLabel2.setFont(new java.awt.Font("Mochiy Pop One", 0, 15)); // NOI18N
        jLabel2.setForeground(new java.awt.Color(157, 229, 248));
        jLabel2.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel2.setText("<html>\nObjective: Your mission is to solve counting puzzles to advance in the game. Each puzzle presents a unique scenario or arrangement of objects, and your task is to accurately count them to find the correct answer.\n<br><br>\nGameplay: Carefully examine each question presented on the screen. Then, use your counting skills to determine the total number of items requested. Once you've counted them, enter your answer.\n<br><br>\nHint System: Stuck on a puzzle? Use your coins to access hints that can provide helpful clues. Earn coins by correctly solving puzzles – the more you solve, the more hints you'll have at your disposal!\n<html>\n\n");
        home.add(jLabel2);
        jLabel2.setBounds(100, 160, 620, 300);

        jLabel4.setFont(new java.awt.Font("Mochiy Pop One", 0, 18)); // NOI18N
        jLabel4.setForeground(new java.awt.Color(157, 229, 248));
        jLabel4.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel4.setText(" The best game for honing your logical skills!");
        home.add(jLabel4);
        jLabel4.setBounds(80, 120, 650, 40);

        jLabel3.setFont(new java.awt.Font("Modak", 0, 48)); // NOI18N
        jLabel3.setForeground(new java.awt.Color(157, 229, 248));
        jLabel3.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel3.setText("Welcome to CountMe!");
        home.add(jLabel3);
        jLabel3.setBounds(80, 70, 650, 70);

        jLabel1.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel1.setIcon(new javax.swing.ImageIcon(getClass().getResource("/countme/Images/tutorial_bg.png"))); // NOI18N
        home.add(jLabel1);
        jLabel1.setBounds(50, 20, 720, 550);

        background.setIcon(new javax.swing.ImageIcon(getClass().getResource("/countme/Images/background.png"))); // NOI18N
        background.setText("sadsadsad");
        home.add(background);
        background.setBounds(0, 0, 801, 600);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(home, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addComponent(home, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(0, 0, Short.MAX_VALUE))
        );

        pack();
        setLocationRelativeTo(null);
    }// </editor-fold>//GEN-END:initComponents

    private void okay_btnActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_okay_btnActionPerformed
        // TODO add your handling code here:
        new tutorial().setVisible(false);
        dispose();
        new CountMe().setVisible(true);
        
        
    }//GEN-LAST:event_okay_btnActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(tutorial.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(tutorial.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(tutorial.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(tutorial.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new tutorial().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JLabel background;
    private javax.swing.JPanel home;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JButton okay_btn;
    // End of variables declaration//GEN-END:variables
}