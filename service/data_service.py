class DataService:
    def get_url(std_name):
        if "Mycoplasma genitalium" in std_name:
            return "https://www.cdc.gov/std/mgen/stdfact-Mgen.htm"
        elif "Pelvic Inflammatory Disease" in std_name:
            return "https://www.cdc.gov/std/pid/stdfact-pid.htm"
        elif "Human Papillomavirus" in std_name:
            return "https://www.cdc.gov/std/hpv/stdfact-hpv.htm"
        elif "Herpes" in std_name:
            return "https://www.cdc.gov/std/herpes/stdfact-herpes.htm"
        elif "HIV/AIDS" in std_name:
            return "https://www.cdc.gov/hiv/basics/index.html"
        elif "Hepatitis C" in std_name:
            return "https://www.cdc.gov/hepatitis/hcv/index.htm"
        elif "Hepatitis B" in std_name:
            return "https://www.cdc.gov/hepatitis/hbv/index.htm"
        elif "Hepatitis A" in std_name:
            return "https://www.cdc.gov/hepatitis/hav/index.htm"
        elif "Neurosyphilis" in std_name:
            return "https://www.cdc.gov/std/treatment-guidelines/neurosyphilis.htm"
        elif "Gonorrhea" in std_name:
            return "https://www.cdc.gov/std/gonorrhea/stdfact-gonorrhea.htm"
        elif "Bacterial Vaginosis" in std_name:
            return "https://www.cdc.gov/std/bv/stdfact-bacterial-vaginosis.htm"
        elif "Chlamydia" in std_name:
            return "https://www.cdc.gov/std/chlamydia/stdfact-chlamydia.htm"
        elif "Trichomoniasis" in std_name:
            return "https://www.cdc.gov/std/trichomonas/stdfact-trichomoniasis.htm"
        elif "Otosyphilis" in std_name:
            return "https://www.cdc.gov/std/treatment-guidelines/neurosyphilis.htm"
        elif "Syphilis" in std_name:
            return "https://www.cdc.gov/std/syphilis/stdfact-syphilis.htm"
        elif "Ocular Syphilis" in std_name:
            return "https://www.cdc.gov/std/treatment-guidelines/neurosyphilis.htm"
        return ""