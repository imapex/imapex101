import sys
import nxtoolkit.nxtoolkit as nx
import json


def main():
    """
    Simple example to output BGP peers in JSON

    set the following environment variables or manually enter credentials when prompted

    export NX_URL=https://nexus-ip
    export NX_LOGIN=admin
    export NX_LOGIN=password


    :return: None
    """
    description = 'messing w/ bgp api'
    creds = nx.Credentials('switch', description)
    args = creds.get()

    ''' Login to Switch '''
    session = nx.Session(args.url, args.login, args.password)
    resp = session.login()

    if not resp.ok:
        print('%% Could not login to Switch')
        sys.exit(0)

    bgp = session.get('/api/node/class/bgpPeer.json')

    ''' GET BGP peers in JSON '''

    print json.dumps(bgp.json()['imdata'], indent=2)

if __name__ == '__main__':
    main()
