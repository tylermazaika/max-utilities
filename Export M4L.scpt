FasdUAS 1.101.10   ��   ��    k             l      ��  ��    � � 
Export a Max for Live Device from Max, and copy it into the folder of Development builds of M4L Devices

Author: Tyler Mazaika
Created: Jan. 2020
     � 	 	(   
 E x p o r t   a   M a x   f o r   L i v e   D e v i c e   f r o m   M a x ,   a n d   c o p y   i t   i n t o   t h e   f o l d e r   o f   D e v e l o p m e n t   b u i l d s   o f   M 4 L   D e v i c e s 
 
 A u t h o r :   T y l e r   M a z a i k a 
 C r e a t e d :   J a n .   2 0 2 0 
   
  
 i         I     �� ��
�� .aevtoappnull  �   � ****  o      ���� 0 argv  ��    k    ]       l     ��������  ��  ��        r         l     ����  n         4    �� 
�� 
cobj  m    ����   o     ���� 0 argv  ��  ��    o      ���� 0 projectname ProjectName      r        l    ����  n         4    �� !
�� 
cobj ! m   	 
����    o    ���� 0 argv  ��  ��    o      ���� 0 buildnamebase BuildnameBase   " # " r     $ % $ l    &���� & n     ' ( ' 4    �� )
�� 
cobj ) m    ����  ( o    ���� 0 argv  ��  ��   % o      ���� .0 includedatenamestring IncludeDateNameString #  * + * l   ��������  ��  ��   +  , - , l    �� . /��   . p j	set ProjectName to "LaunchpadController"	set BuildnameBase to "DEV"	set IncludeDateNameString to "1"
	    / � 0 0 �  	 s e t   P r o j e c t N a m e   t o   " L a u n c h p a d C o n t r o l l e r "  	 s e t   B u i l d n a m e B a s e   t o   " D E V "  	 s e t   I n c l u d e D a t e N a m e S t r i n g   t o   " 1 " 
 	 -  1 2 1 l   ��������  ��  ��   2  3 4 3 l   ��������  ��  ��   4  5 6 5 l    �� 7 8��   7 "  Script for file deployment     8 � 9 9 8   S c r i p t   f o r   f i l e   d e p l o y m e n t   6  : ; : r     < = < m     > > � ? ? b / U s e r s / t y l e r / d e v / m a x - u t i l i t i e s / d e p l o y _ m 4 l _ a m x d . p y = o      ���� 0 deploy_script   ;  @ A @ r     B C B m     D D � E E 8 / U s e r s / t y l e r / b u i l d / m 4 l _ a m x d / C o      ���� 0 	amxd_path   A  F G F l   ��������  ��  ��   G  H I H l    �� J K��   J !  Get date and set filename     K � L L 6   G e t   d a t e   a n d   s e t   f i l e n a m e   I  M N M Z    @ O P�� Q O =     R S R o    ���� .0 includedatenamestring IncludeDateNameString S m     T T � U U  1 P k   # 6 V V  W X W r   # * Y Z Y l  # ( [���� [ I  # (�� \��
�� .sysoexecTEXT���     TEXT \ m   # $ ] ] � ^ ^ * d a t e   ' + % Y % m % d _ % H % M % S '��  ��  ��   Z o      ���� 0 date_string   X  _�� _ r   + 6 ` a ` b   + 4 b c b b   + 2 d e d b   + 0 f g f b   + . h i h o   + ,���� 0 projectname ProjectName i m   , - j j � k k  - g o   . /���� 0 buildnamebase BuildnameBase e m   0 1 l l � m m  _ c o   2 3���� 0 date_string   a o      ���� 0 	file_name  ��  ��   Q r   9 @ n o n b   9 > p q p b   9 < r s r o   9 :���� 0 projectname ProjectName s m   : ; t t � u u  - q o   < =���� 0 buildnamebase BuildnameBase o o      ���� 0 	file_name   N  v w v r   A L x y x b   A H z { z b   A D | } | o   A B���� 0 	amxd_path   } o   B C���� 0 	file_name   { m   D G ~ ~ �   
 . a m x d y o      ���� 0 amxd_full_path   w  � � � l  M M��������  ��  ��   �  � � � l  M M��������  ��  ��   �  � � � I  M T�� ���
�� .ascrcmnt****      � **** � o   M P���� 0 amxd_full_path  ��   �  � � � l  U U�� � ���   �   error number -5    � � � �     e r r o r   n u m b e r   - 5 �  � � � l  U U��������  ��  ��   �  � � � O  U a � � � I  [ `������
�� .miscactvnull��� ��� null��  ��   � m   U X � �t                                                                                  max2  alis      Macintosh HD                   BD ����Max.app                                                        ����            ����  
 cu             Applications  /:Applications:Max.app/     M a x . a p p    M a c i n t o s h   H D  Applications/Max.app  / ��   �  � � � I  b g�� ���
�� .sysodelanull��� ��� nmbr � m   b c���� ��   �  � � � l  h h��������  ��  ��   �  � � � l  h h�� � ���   � 6 0 custom keyboard shortcut for "Export..." dialog    � � � � `   c u s t o m   k e y b o a r d   s h o r t c u t   f o r   " E x p o r t . . . "   d i a l o g �  � � � O  h � � � � I  n ��� � �
�� .prcskprsnull���     ctxt � m   n q � � � � �  e � �� ���
�� 
faal � J   t  � �  � � � m   t w��
�� eMdsKcmd �  � � � m   w z��
�� eMdsKopt �  ��� � m   z }��
�� eMdsKctl��  ��   � m   h k � ��                                                                                  sevs  alis    \  Macintosh HD                   BD ����System Events.app                                              ����            ����  
 cu             CoreServices  0/:System:Library:CoreServices:System Events.app/  $  S y s t e m   E v e n t s . a p p    M a c i n t o s h   H D  -System/Library/CoreServices/System Events.app   / ��   �  � � � l  � ���������  ��  ��   �  � � � l  � ���������  ��  ��   �  � � � l   � ��� � ���   � / ) Wait for Save (Export) window to appear     � � � � R   W a i t   f o r   S a v e   ( E x p o r t )   w i n d o w   t o   a p p e a r   �  � � � O   � � � � � W   � � � � � I  � ��� ���
�� .sysodelanull��� ��� nmbr � m   � ����� ��   � l  � � ����� � I  � ��� ���
�� .coredoexnull���     **** � n   � � � � � 4   � ��� �
�� 
cwin � m   � � � � � � �  S a v e � 4   � ��� �
�� 
pcap � m   � � � � � � �  M a x��  ��  ��   � m   � � � ��                                                                                  sevs  alis    \  Macintosh HD                   BD ����System Events.app                                              ����            ����  
 cu             CoreServices  0/:System:Library:CoreServices:System Events.app/  $  S y s t e m   E v e n t s . a p p    M a c i n t o s h   H D  -System/Library/CoreServices/System Events.app   / ��   �  � � � I  � ��� ���
�� .sysodelanull��� ��� nmbr � m   � ����� ��   �  � � � l  � ���������  ��  ��   �  � � � l  � ��� � ���   � U O TODO: make sure we are saving into the correct folder ?  cmd-shift-g for go-to    � � � � �   T O D O :   m a k e   s u r e   w e   a r e   s a v i n g   i n t o   t h e   c o r r e c t   f o l d e r   ?     c m d - s h i f t - g   f o r   g o - t o �  � � � l  � ���������  ��  ��   �  � � � l   � ��� � ���   � %  Replace name in Export dialog     � � � � >   R e p l a c e   n a m e   i n   E x p o r t   d i a l o g   �  � � � O   � � � � � k   � � � �  � � � O   � � � � � r   � � � � � o   � ����� 0 	file_name   � n       � � � 1   � ���
�� 
valL � n   � � � � � 4   � ��� �
�� 
txtf � m   � �����  � 4   � ��� �
�� 
cwin � m   � �����  � 4   � ��� �
�� 
prcs � m   � � � � � � �  M a x �  � � � I  � ��� ���
�� .sysodelanull��� ��� nmbr � m   � ����� ��   �  � � � l  � �� � ��   �   Press Return    � � � �    P r e s s   R e t u r n �  ��~ � I  � ��} ��|
�} .prcskcodnull���     **** � m   � ��{�{ $�|  �~   � m   � � � ��                                                                                  sevs  alis    \  Macintosh HD                   BD ����System Events.app                                              ����            ����  
 cu             CoreServices  0/:System:Library:CoreServices:System Events.app/  $  S y s t e m   E v e n t s . a p p    M a c i n t o s h   H D  -System/Library/CoreServices/System Events.app   / ��   �  � � � l  � ��z�y�x�z  �y  �x   �  � � � l  � ��w�v�u�w  �v  �u   �  � � � l   � ��t � ��t   � + % Wait and check for creation of file     � �   J   W a i t   a n d   c h e c k   f o r   c r e a t i o n   o f   f i l e   �  r   � � m   � ��s�s   o      �r�r 0 did_find_file    U   �% k   � 		 

 r   �
 l  ��q�p I  ��o�n
�o .sysoexecTEXT���     TEXT b   � b   � � m   � � � 
 [   - e   o   � ��m�m 0 amxd_full_path   m   � � ,   ]   & &   e c h o   1   | |   e c h o   0�n  �q  �p   o      �l�l 0 did_find_file    Z  �k�j =  o  �i�i 0 did_find_file   m   �  1  S  �k  �j    �h  I  �g!�f
�g .sysodelanull��� ��� nmbr! m  �e�e �f  �h   m   � ��d�d  "#" l &&�c�b�a�c  �b  �a  # $%$ l &&�`�_�^�`  �_  �^  % &'& l &&�]�\�[�]  �\  �[  ' ()( Z  &[*+�Z,* > &--.- o  &)�Y�Y 0 did_find_file  . m  ),// �00  1+ I 0;�X1�W
�X .sysodisAaleR        TEXT1 b  07232 m  0344 �55 H U n a b l e   t o   l o c a t e   f i l e   b u i l t   f i l e .   
 
3 o  36�V�V 0 amxd_full_path  �W  �Z  , k  >[66 787 I >I�U9:
�U .sysonotfnull��� ��� TEXT9 o  >?�T�T 0 	file_name  : �S;�R
�S 
appr; m  BE<< �== ( E x p o r t   M 4 L   S u c c e e d e d�R  8 >?> I JY�Q@�P
�Q .sysoexecTEXT���     TEXT@ b  JUABA b  JQCDC b  JOEFE o  JK�O�O 0 deploy_script  F m  KNGG �HH    - nD o  OP�N�N 0 projectname ProjectNameB m  QTII �JJ    - d   - l�P  ? KLK l ZZ�M�L�K�M  �L  �K  L MNM l ZZ�JOP�J  O D > Update in Ableton immediately, but only if Ableton is running   P �QQ |   U p d a t e   i n   A b l e t o n   i m m e d i a t e l y ,   b u t   o n l y   i f   A b l e t o n   i s   r u n n i n gN R�IR l ZZ�HST�H  S ; 5 tell application "Ableton Live 10 Suite" to activate   T �UU j   t e l l   a p p l i c a t i o n   " A b l e t o n   L i v e   1 0   S u i t e "   t o   a c t i v a t e�I  ) V�GV l \\�F�E�D�F  �E  �D  �G    WXW l     �C�B�A�C  �B  �A  X Y�@Y l     �?�>�=�?  �>  �=  �@       �<Z[�<  Z �;
�; .aevtoappnull  �   � ****[ �: �9�8\]�7
�: .aevtoappnull  �   � ****�9 0 argv  �8  \ �6�6 0 argv  ] 5�5�4�3�2 >�1 D�0 T ]�/�. j l�- t ~�,�+ ��*�) � ��(�'�&�%�$�# ��" ��!�  �������/4��<�GI
�5 
cobj�4 0 projectname ProjectName�3 0 buildnamebase BuildnameBase�2 .0 includedatenamestring IncludeDateNameString�1 0 deploy_script  �0 0 	amxd_path  
�/ .sysoexecTEXT���     TEXT�. 0 date_string  �- 0 	file_name  �, 0 amxd_full_path  
�+ .ascrcmnt****      � ****
�* .miscactvnull��� ��� null
�) .sysodelanull��� ��� nmbr
�( 
faal
�' eMdsKcmd
�& eMdsKopt
�% eMdsKctl
�$ .prcskprsnull���     ctxt
�# 
pcap
�" 
cwin
�! .coredoexnull���     ****
�  
prcs
� 
txtf
� 
valL� $
� .prcskcodnull���     ****� 0 did_find_file  � 
� .sysodisAaleR        TEXT
� 
appr
� .sysonotfnull��� ��� TEXT�7^��k/E�O��l/E�O��m/E�O�E�O�E�O��  �j 
E�O��%�%�%�%E�Y 	��%�%E�O��%a %E` O_ j Oa  *j UOkj Oa  a a a a a mvl UOa  $ !h*a a /a a  /j !kj [OY��UOkj Oa  -*a "a #/ �*a k/a $k/a %,FUOkj Oa &j 'UOjE` (O 6a )kha *_ %a +%j 
E` (O_ (a ,  Y hOkj [OY��O_ (a - a ._ %j /Y �a 0a 1l 2O�a 3%�%a 4%j 
OPOP ascr  ��ޭ