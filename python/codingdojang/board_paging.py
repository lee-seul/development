# coding: utf-8
# 001_board_paging.py

def paging(m, n):
	page = m//n
	if m % n != 0:
		page += 1
	return page

m = int(input(u'총 건수'))
n = int(input(u'페이지 당 게시물 수 '))


print(u'총 페이지수: %d' % paging(m, n))
