#coding:gbk
"""
Ŀ�꣺RPSLS��Ϸ��ʯͷ����������ʷ���ˣ�
���ߣ�����
���ڣ�2021��6��5��
"""

import random
def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
        return 0;
    elif name=="ʷ����":
        return 1
    elif name=="��":
        return 2
    elif name=="����":
        return 3
    else:
        return 4

def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
        return "ʯͷ"
    elif number==1:
        return "ʷ����"
    elif number==2:
        return "��"
    elif number==3:
        return "����"
    else:
        return "����"
    pass 

def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """
    print("���ѡ���ǣ�",player_choice)
    a=name_to_number(player_choice)
    b=random.randint(0,4)
    s1=number_to_name(b)
    print("������ѡ���ǣ�",s1)
    comp(a,b)
    
def comp(a,b):
    if a==b:
        print("���ͼ��������һ����")
    if a==0 and (b==3 or b==4):
        print("��ϲ��Ӯ�ˣ�")
    if a==0 and (b==1 or b==2):
        print("������˼����Ӯ��~")
    if a==1 and (b==0 or b==4):
        print("��ϲ��Ӯ�ˣ�")   
    if a==1 and (b==2 or b==3):
        print("������˼����Ӯ��~")
    if a==2 and (b==0 or b==1):
        print("��ϲ��Ӯ�ˣ�")   
    if a==2 and (b==3 or b==4):
        print("������˼����Ӯ��~")
    if a==3 and (b==1 or b==2):
        print("��ϲ��Ӯ�ˣ�")   
    if a==3 and (b==0 or b==4):
        print("������˼����Ӯ��~")
    if a==4 and (b==2 or b==3):
        print("��ϲ��Ӯ�ˣ�")   
    if a==4 and (b==0 or b==1):
        print("������˼����Ӯ��~")
# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
choice_name=input("���������ѡ��")
rpsls(choice_name)
input()
