#!/usr/bin/env bash
cat codes_insee.txt | tail -n+2 | cut -f 1 | while read l; do
    # Because the AMF changes the INSEE number
    lname="$(echo $l | sed 's/^2A/20/' | sed 's/^2B/20/' )"
    wget "http://www.amf.asso.fr/annuaire/index.asp?refer=commune&dep_n_id=&NUM_INSEE=$lname" -O "website/iso-$l";
    iconv -f iso8859-1 -t utf8 website/iso-$l > website/$l
    rm website/iso-$l
done
