#!/bin/bash

EXIT=0
for dockerfile in $@; do
    for argname in $(grep -E '^ARG [_[:alnum:]]{1,}=' $dockerfile | sort | sed 's/^ARG \([_[:alnum:]]\{1,\}\).*/\1/' | uniq); do
        if [[ $(grep -E "^ARG $argname=" $dockerfile | uniq | wc -l) -gt 1 ]]; then
            echo "Found multiple ARG $argname in $dockerfile with different values:" >&2
            grep -n "^ARG $argname=" $dockerfile
            echo >&2
            echo "Please update both/all ARG $argname directives to the same value in $dockerfile." >&2
            echo >&2
            echo "You can also temporarily disable this check by setting SKIP=check-different-arg-values." >&2
            EXIT=$(( $EXIT + 1 ))
        fi
    done
done
exit $EXIT
