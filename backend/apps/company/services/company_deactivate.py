



class CompanyDeactivateService:
    @staticmethod
    def execute(*, company, user, hard_deleted: bool = False):
        """
        User Case 9: Deactivate or Delete Company

        as'uliyatlar: Kompaniyani o'chirish (yumshoq o'chirish) Agar hard_delete=True bo'lsa,
        kompaniyani butunlay o'chirish. Ushbu amalni faqat EGASI bajarishi mumkinligiga ishonch hosil qiling.
        """
        raise NotImplementedError("CompanyDeactivateService not implemented yet")