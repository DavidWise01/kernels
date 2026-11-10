"""ECK-011: chromatic calibration continuity, standard-library test model.

No hardware calibration or independent witness signatures are claimed.
"""
import hashlib, json, copy

def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")

def digest(sample):
    return hashlib.sha256(bytes([0]) + canonical(sample)).hexdigest()

def seal(position, hue, wavelength, chronos):
    if not all(isinstance(v, int) and not isinstance(v,bool) for v in (position,hue,wavelength,chronos)):
        raise ValueError("integer readings required")
    if not (0 <= position <= 359 and 0 <= hue <= 359 and 380 <= wavelength <= 750 and 0 <= chronos <= 999):
        raise ValueError("out-of-range observation")
    record = dict(primitive="observed-chrome-v1", position_deg=position,
                  hue_deg=hue, wavelength_nm=wavelength, chronos_ms=chronos)
    return record, digest(record)

def calibrate(record, parent_hash, offset_nm):
    if digest(record) != parent_hash:
        raise ValueError("raw measurement digest mismatch")
    if type(offset_nm) is not int or not -60 <= offset_nm <= 60:
        raise ValueError("calibration offset outside supported range")
    return dict(type="calibration", parent_leaf=parent_hash,
                calibration_id="wavelength-offset-v1", wavelength_offset_nm=offset_nm,
                interpreted_wavelength_nm=record["wavelength_nm"] + offset_nm)

def verify(record, parent_hash, derived):
    return (digest(record) == parent_hash
            and derived.get("parent_leaf") == parent_hash
            and derived.get("calibration_id") == "wavelength-offset-v1"
            and type(derived.get("wavelength_offset_nm")) is int
            and -60 <= derived["wavelength_offset_nm"] <= 60
            and derived.get("interpreted_wavelength_nm") ==
                record["wavelength_nm"] + derived["wavelength_offset_nm"])

def test():
    n = 0
    def check(x, label):
        nonlocal n
        assert x, label
        n += 1
    raw, original = seal(180,28,590,250)
    check(digest(raw) == original,"seal digest")
    a = calibrate(raw, original, +5)
    b = calibrate(raw, original, -20)
    check(verify(raw,original,a),"first interpretation")
    check(verify(raw,original,b),"second interpretation")
    check(a["interpreted_wavelength_nm"] == 595,"positive offset")
    check(b["interpreted_wavelength_nm"] == 570,"negative offset")
    check(digest(raw) == original,"no raw mutation")
    modified=copy.deepcopy(raw);modified["wavelength_nm"] += 1
    check(not verify(modified,original,a),"mutated wavelength")
    modified=copy.deepcopy(raw);modified["chronos_ms"] += 1
    check(not verify(modified,original,a),"mutated time")
    modified=copy.deepcopy(raw);modified["hue_deg"] += 1
    check(not verify(modified,original,a),"mutated hue")
    modified=copy.deepcopy(a);modified["parent_leaf"]="0"*64
    check(not verify(raw,original,modified),"parent substitution")
    modified=copy.deepcopy(a);modified["interpreted_wavelength_nm"] = 600
    check(not verify(raw,original,modified),"derived substitution")
    for bad in [-61,61,1.5,True]:
        try: calibrate(raw,original,bad)
        except ValueError: check(True,"offset rejected")
        else: check(False,"offset not rejected")
    try: seal(180,28,751,250)
    except ValueError: check(True,"observation range rejected")
    else: check(False,"range accepted")
    print(f"ECK-011: {n}/{n} calibration-continuity assertions PASS")
if __name__ == "__main__": test()
