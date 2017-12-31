#! /bin/sh

# publish build packages to repository. These should be set in your
# ~/.bashrc:
# 	DEBREPOUSER
#		DEBREPOHOST
# 	DEBREPODIR

scp $@ ${DEBREPOUSER}@${DEBREPOHOST}:${DEBREPODIR}/pool/main/
ssh ${DEBREPOUSER}@${DEBREPOHOST} "cd ${DEBREPODIR}; reindex_apt.sh"
