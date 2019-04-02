package sback.invoice;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.List;

public class InvoiceFilterTest {
    @Test
    void filterInvoices() {

        InvoiceDao dao = new InvoiceDao();
        Invoice alberto = new Invoice("Alberto", 20.0);
        Invoice fabio = new Invoice("Fabio", 300.0);

        dao.save(alberto);
        dao.save(fabio);

        InvoiceFilter filter = new InvoiceFilter();
        List<Invoice> result = filter.filter();

        Assertions.assertEquals(alberto, result.get(0));
        Assertions.assertEquals(1, result.size());

        dao.close();
    }

}