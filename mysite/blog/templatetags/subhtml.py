from django import template
register=template.Library()

@register.filter()
def subhtml(str,arg):
	length=int(arg)
	i=-1
	l=len(str)
	count=0
	stack=[]
	while i<l-1 and (count<length or len(stack)>0):
		i=i+1
		char=str[i]
		if char==' ' or char=='\n' or char=="\t" or char=='\r':
			continue
		if char=='<':
			isBeginTag=True
			if str[i+1]=='/':
				i=i+1
				isBeginTag=False
			start=i+1
			while str[i]!='>':
				i=i+1
			last=start
			while str[last]!=' ' and str [last]!='/' and str[last]!='>':
				last=last+1
			if str[i-1]!='/':
				tagName=str[start:last]
				if isBeginTag:
					stack.insert(0,tagName)
				else:
					stack.remove(tagName)
			continue
		else:
			count=count+1	
	return str[:i+1]
