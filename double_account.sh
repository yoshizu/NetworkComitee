#!/bin/sh

echo -n "RealName"
read NAME
echo -n "ISCaccount"
read ISCaccount
echo -n "Account"
read Account
sendMailx() {
	from="$1"
	to="$2"
	cc="$3"
	bcc="$4"
	subject="$5"
	contents="$6"

	inputEncoding="utf-8"
	outputEncoding="utf-8"
	subjectHead="=?$outputEncoding?B?"
	subjectBody="`echo "$subject" | iconv -f $inputEncoding -t $outputEncoding | base64 | tr -d '\n'`"
	subjectTail="?="
	fullSubject="$subjectHead$subjectBody$subjectTail"
	mailContens="`printf "$contents" | iconv -f $inputEncoding -t $outputEncoding`"
	echo "$mailContens" | mailx -s "$fullSubject" -c "$cc" -b "$bcc"  "$to" -S replyto="admin@club.kyutech.ac.jp"
	return $?
}

#test
from="yoshizu@club.kyutech.ac.jp"
to="'ISCaccount@club.kyutech.ac.jp"
cc=""
bcc=""
subject="アカウント登録について"
contents="学生自治ネットワーク委員会運用部の[送信者名]です。

                $NAME様

共用計算機のアカウント発行申請を受け付けました。
しかし、$NAME 様はすでに $Account というアカウントを所持しております。

アカウントの重複取得は、共用計算機利用規約第３条３項
(http://www.club.kyutech.ac.jp/w/共用計算機利用規約)
により禁止されていますので、アカウント [登録済みのアカウント名] を使用していただきますよう、お願いします。

パスワード紛失等による再発行は、 課外活動共用施設共用室3で受け付けています。
あらかじめ運用部宛にメール( admin@club.kyutech.ac.jp ) で、運用部員在室時間の確認をした上、
身分確認のために学生証を持参してお越しください。

この件につきまして、質問等がございましたら admin@club.kyutech.ac.jp までお願いします。

-- 
九州工業大学 学生自治ネットワーク委員会
中原　禎和 <Yoshikazu NAKAHARA>
Mail: yoshizu@club.kyutech.ac.jp"
sendMailx "$from" "$to" "$cc" "$bcc" "$subject" "$contents"
if [ $? -eq 1 ]; then
	echo "send mail failure"
	exit 1
fi
echo "send mail success"
