ORIG_SCANNER_V2=orig-scan-v2.l   # 2.7.2 scanner
ORIG_SCANNER_V3=orig-scan-v3.l   # 3.3.0 scanner


all: v2 v3

v2: 2.0.l 2.2.l 2.3.l 2.4.l 2.4.3.l 2.5.l 2.6.l 2.7.l 2.7.2.l

v3: 3.0.l 3.1.l 3.2.l 3.3.0.l 3.5.0.l 3.6.0.l

# 2.5 and after are just the same as the v2 scanner:
2.5.l 2.6.l 2.7.l 2.7.2.l: $(ORIG_SCANNER_V2)
	cp $< $@

# 2.4, 2.4.3 missing as, with
2.4.l 2.4.3.l: $(ORIG_SCANNER_V2)
	egrep -v '^"(as|with)"' $< >$@

# 2.2, 2.3 also missing @
2.2.l 2.3.l: 2.4.l
	egrep -v '^"@"' $< >$@

# 2.0 also missing yield, //, //= 
2.0.l: 2.2.l
	egrep -v '^"(yield|//|//=)"' $< >$@



# 3.1 and 3.2 mustn't allow u as unicode literal prefix:
3.1.l 3.2.l: $(ORIG_SCANNER_V3)
	sed -e '/^stringprefix/c\
stringprefix  {rbprefix}' $< >$@

# 3.0 is same as 3.1/3.2 except for <>:
3.0.l: $(ORIG_SCANNER_V3)
	sed -e '/^stringprefix/c\
stringprefix  {rbprefix}' $<  | egrep -v '^"(<>)"'  >$@

# 3.3 is the same as the v3 scanner:
3.3.0.l: $(ORIG_SCANNER_V3)
	cp $< $@

# 3.5 and after add: @=, async, await
3.5.0.l: $(ORIG_SCANNER_V3)
	sed -e '/^{name}/i\
"@="       { return ATEQ; } \
"await"    { return AWAIT; } \
"async"    { return ASYNC; }' $< >$@

# 3.6.0 allows 'f' as string prefix
3.6.0.l: 3.5.0.l
	sed -e '/^ruprefix/c\
ruprefix      [rRuUfF]|[rRfF][rRfF]' $< >$@

clean:
	$(RM) [23].*.l


