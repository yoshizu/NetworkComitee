# -*- coding: utf- -*-
from smtplib import SMTP
from email.message import Message
from email.header import Header
from email.mime.text import MIMEText
import email.utils
import sys
import codecs

if __name__ == "__main__":
	host = "lapis.club.kyutech.ac.jp"
	port = 587
	print("Type new user ISC account.")
	iscAccount = input()
	print("Type new user account.")
	newAccount = input()
	sys.stdin = codecs.getreader('utf-8')(sys.stdin)
	print("Type new user name.")
	newUser = input()
	sys.stdin = codecs.getreader('ascii')(sys.stdin)
	from_address = "yoshizu@club.kyutech.ac.jp"
	charset = "ISO-2022-JP"
	subject = u"アカウント登録完了のお知らせ"
	body    = u"学生自治ネットワーク委員会運用部の中原です。\n                " + newUser + u" 様\n共用計算機のアカウント登録が完了しました。\nアカウント名は" + newAccount + u"です。\n\n利用するにあたっては、各規約を順守してください。\n→ http://www.club.kyutech.ac.jp/w/利用規約\nまた、情報科学センターからリモートログインして利用する場合は、\nsshコマンドを利用します。sshはすべての通信内容を暗号化します。\n\n例：\nssh remote.club.kyutech.ac.jp -l 共用計算機のアカウント名\n\nその他のOS(Windows,Macなど)から接続する場合には、利用マニュアルをご覧ください。\n→ http://www.club.kyutech.ac.jp/w/SSH\n"
	body += "\n教務情報システムの利用方法については、以下のページを参照してください\n→ http://www.club.kyutech.ac.jp/w/RDP\n\n共用計算機では以下のサービスを提供しております。\n\n◯Webページの公開あなたのホームディレクトリの下に「www」というディレクトリを作り、そこにドキュメントを設置することで、Webページを公開することができます。詳しくは以下のURLをご覧下さい。\n→ http://www.club.kyutech.ac.jp/w/個人Webサイトの利用\n\nただし、個人向けWebページのサービスなので、個人のディレクトリの下に団体のWebページを設置することは禁止されています。団体のWebページの開設に関してはこちらのURLをご覧下さい。\n→ http://www.club.kyutech.ac.jp/w/団体webサイトの申請\n\n◯メールアドレスの取得あなたのアカウント名に@club.kyutech.ac.jpを加えたものがメールアドレスとなります。共用計算機ではMuttを標準メーラーとしており、muttコマンドで使用できます。外部からメールを取得する場合は、利用マニュアルをご覧ください。\n→ http://www.club.kyutech.ac.jp/w/Mutt\nまた、Webメーラーを利用する事もできます。\n→ https://webmail.club.kyutech.ac.jp/roundcube/\n運用部ではお知らせをメールで送ることがありますので、定期的に共用計算機アカウント宛てのメールを確認して下さい。\nなお、初期設定ではあなたの ISC のメールアドレスへすべてのメールが転送されるように設定されています。この設定を変更するには利用マニュアルをご覧ください。\n→ http://www.club.kyutech.ac.jp/w/Forward\n\n■利用上の注意\nアカウントを他人に貸したり、パスワードを教えることは絶対にしないでください。このような行為はセキュリティ上非常に危険なため発見次第アカウントを停止致します。また、パスワードを紙等に書き留めることも危険ですので絶対に避けてください。\n\n■申請した覚えのない方へ\n上記のアカウントを申請した覚えのない方は、\nadmin@club.kyutech.ac.jp 宛にその旨のメールを送ってください。\nお手数をおかけしますが宜しくお願いします。\n\n質問等は admin@club.kyutech.ac.jp で受け付けています。\n\n-- \n九州工業大学 学生自治ネットワーク委員会\n中原　禎和 <Yoshikazu NAKAHARA>\nMail: yoshizu@club.kyutech.ac.jp"

	MAIL_SERVER = "lapis.club.kyutech.ac.jp"
	ENCODING = "iso-2022-jp"
	to_email1 = newAccount + "@club.kyutech.ac.jp"
	#to_email1 = to_email1.encode(ENCODING)
	to_email2 = iscAccount + "@mail.kyutech.jp"
	#to_email2 = to_email2.encode(ENCODING)
	msg = MIMEText(body,"plain",charset)
	msg["Subject"] = Header(subject,charset)
	msg["From"]    = from_address
	msg['To'] = to_email1 + "," + to_email2
	msg["Date"] = email.utils.formatdate(localtime=True)
	REPLY_TO_ADDRESS = 'admin@club.kyutech.ac.jp'
	msg.add_header('reply-to', REPLY_TO_ADDRESS)

	smtpserver = SMTP(MAIL_SERVER)
	try:
		smtpserver.set_debuglevel(True)
# 自分自身を識別してサポートしている機能をサーバに入力させる
		smtpserver.ehlo()
# このセッションを暗号化できるならそうする
		if smtpserver.has_extn('STARTTLS'):
			smtpserver.starttls()
			#smtpserver.login(username, password)
			smtpserver.ehlo() # TLS コネクションで自分自身を再識別する
			smtpserver.sendmail(MAIL_SERVER, [to_email1, to_email2], msg.as_string())
	except:
		raise
	finally:
		smtpserver.quit()
