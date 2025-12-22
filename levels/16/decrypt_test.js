const sjcl = require('/home/user/manik/node_modules/sjcl');

const encryptedRaw = "EnCt29461dc1f9e7e9e5e1d20996c137e37288f0ee0fc9461dc1f9e7e9e5e1d20996cbwfLn5phXAOG3y3ywVIzEAJtmVQtPkf3c3YRsBBrHTsOL1kikoXyBLw8rIuwFSLxInl+YftuWhrKycVrGZvfVShP3g7czpb0tjFH5Ov7B7YfSsJqH43WmfnRfBSu5sbLU+SCzdf4shm6U9ZWlunnJOoVaiRdq110riVpiwxy8Nt1eLbgxvRBHwZQaVwY5jqlKH/KKn4zequ4f9eedd3pMfGMdcLxm8XlbXxyCHlPGRtNUTiMp4FAIlFyzzhArIRDcEMaI+Ex3kWdkZ7zzaTbC87C2mddGRvksHfeGOGTKbaKQVFQlbfaen3Uc5FWQbwJMVFb3vK2g+kfdwSQbZpQmd2lcQkdCY51uDivNvMa6W7SbebG7ItNyhxRcRN+Ct9v1BMhmAggQcGQ3cDpOQq8AZGBqy/l2pc1o0yrPiDiedmHuFA5c+Xu8HeqpkdTKSDv8fXrqNGMxYpMLUnIhcs=IwEmS";

const content = encryptedRaw.slice(4, -5);
const hexPart = content.slice(0, 64);
const b64Part = content.slice(64);

const passwords = [
    "iveco", "IVECO", "crossway", "CROSSWAY", "karosa", "KAROSA",
    "sad", "SAD", "sadzvolen", "zvolen", "ZVOLEN",
    "irisbus", "IRISBUS", "sodomka", "SODOMKA",
    "test", "password", "heslo", "kluc", "abc123", "123abc",
    "turcandelta", "delta", "spz", "ecv", "autobus", "bus"
];

console.log("Testing SJCL decrypt...");

for (const pwd of passwords) {
    // Try different SJCL cipher configurations
    const configs = [
        { mode: "ccm", ts: 64, ks: 256, iter: 1000 },
        { mode: "ccm", ts: 64, ks: 128, iter: 1000 },
        { mode: "gcm", ts: 128, ks: 256, iter: 1000 },
        { mode: "ocb2", ts: 64, ks: 256, iter: 1000 },
    ];

    for (const config of configs) {
        try {
            const ct = {
                iv: hexPart.slice(32, 64),
                salt: hexPart.slice(0, 32),
                ct: b64Part,
                ...config
            };
            const result = sjcl.decrypt(pwd, JSON.stringify(ct));
            console.log("FOUND with " + pwd + " (" + config.mode + "): " + result.substring(0, 200));
            process.exit(0);
        } catch(e1) {
            try {
                const ct2 = {
                    salt: hexPart,
                    ct: b64Part,
                    ...config
                };
                const result2 = sjcl.decrypt(pwd, JSON.stringify(ct2));
                console.log("FOUND (method2) with " + pwd + ": " + result2.substring(0, 200));
                process.exit(0);
            } catch(e2) {
                // Silent
            }
        }
    }
}

console.log("No match found with SJCL");
