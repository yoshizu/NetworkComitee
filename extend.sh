#!/bin/sh
#PW=@rcAd1@
echo -n "Username:"
read account
echo -n "Schoolaccount:"
read schoolaccount
account() {
/usr/club/sbin/ldapentry add $account
}
staff_account() {
/usr/club/sbin/ldapentry staff $account
sudo su - $account
Forward=/home/club/$account/forward.sh
if [ -e $Forward ];then
sh $Forward
else
echo -e "$Schoolaccount@mail.kyutech.jp\n$account@club.kyutech.ac.jp" | cat > /home/club/$account/.forward
fi
logout
}

if [ -e /home/staff/CIA/admin-sys/shinsei/ldif/$account ]; then
vim /home/staff/CIA/admin-sys/shinsei/ldif/$account 
fi
account  $account
if [ $? -eq 0 ];then
ldapsearch -x uid=$account
fi
